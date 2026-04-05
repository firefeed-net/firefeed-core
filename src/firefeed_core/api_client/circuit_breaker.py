"""
Circuit Breaker implementation for FireFeed Core

Provides fault tolerance by preventing requests to failing services.
"""

import asyncio
import time
from enum import Enum
from typing import Dict, Any


class CircuitState(Enum):
    """Circuit breaker states."""
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Blocking requests
    HALF_OPEN = "half_open"  # Testing if service recovered


class CircuitBreaker:
    """
    Circuit breaker implementation to prevent cascading failures.

    States:
    - CLOSED: Normal operation, all requests pass through
    - OPEN: Service is failing, block all requests
    - HALF_OPEN: Allow limited requests to test recovery
    """

    def __init__(
        self,
        failure_threshold: int = 5,
        timeout: int = 60,
        recovery_timeout: int = 30,
        success_threshold: int = 3,
        half_open_max_requests: int = 1
    ):
        """
        Initialize circuit breaker.

        Args:
            failure_threshold: Number of failures to open circuit
            timeout: Time in seconds before trying to close circuit
            recovery_timeout: Time in half-open state before returning to closed
            success_threshold: Number of successes needed to close circuit from half-open
            half_open_max_requests: Maximum concurrent requests allowed in half-open state
        """
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.recovery_timeout = recovery_timeout
        self.success_threshold = success_threshold
        self.half_open_max_requests = half_open_max_requests

        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.half_open_request_count = 0  # Track concurrent requests in HALF_OPEN
        self.last_failure_time = None
        self.last_success_time = None
        self.last_state_change = time.time()
        
        # Lock for thread-safe state transitions
        self._lock = asyncio.Lock()
    
    def allow_request(self) -> bool:
        """
        Check if request should be allowed based on circuit state.

        Returns:
            True if request should be allowed, False otherwise
        """
        current_time = time.time()

        # State transitions
        if self.state == CircuitState.OPEN:
            # Check if timeout has passed, move to half-open
            if current_time - self.last_state_change >= self.timeout:
                self.state = CircuitState.HALF_OPEN
                self.success_count = 0
                self.half_open_request_count = 0
                self.last_state_change = current_time
                return True
            return False

        elif self.state == CircuitState.HALF_OPEN:
            # Allow limited concurrent requests in half-open state
            if self.half_open_request_count < self.half_open_max_requests:
                self.half_open_request_count += 1
                return True
            return False

        else:  # CLOSED
            return True
    
    def record_success(self):
        """Record successful request."""
        current_time = time.time()
        self.last_success_time = current_time

        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.success_threshold:
                self.state = CircuitState.CLOSED
                self.failure_count = 0
                self.half_open_request_count = 0
                self.last_state_change = current_time
        elif self.state == CircuitState.CLOSED:
            # Don't decrement failure_count on successes in CLOSED state
            # This prevents the circuit from staying closed when there are intermittent failures
            pass

    async def async_record_success(self):
        """Thread-safe version of record_success."""
        async with self._lock:
            self.record_success()

    def record_failure(self):
        """Record failed request."""
        current_time = time.time()
        self.last_failure_time = current_time
        self.failure_count += 1

        if self.state == CircuitState.CLOSED:
            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN
                self.last_state_change = current_time

        elif self.state == CircuitState.HALF_OPEN:
            # Return to open state on failure in half-open
            self.state = CircuitState.OPEN
            self.half_open_request_count = 0
            self.last_state_change = current_time

    async def async_record_failure(self):
        """Thread-safe version of record_failure."""
        async with self._lock:
            self.record_failure()
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Get circuit breaker statistics.
        
        Returns:
            Dictionary with circuit breaker stats
        """
        return {
            "state": self.state.value,
            "failure_count": self.failure_count,
            "success_count": self.success_count,
            "last_failure_time": self.last_failure_time,
            "last_success_time": self.last_success_time,
            "last_state_change": self.last_state_change,
            "failure_threshold": self.failure_threshold,
            "timeout": self.timeout,
            "recovery_timeout": self.recovery_timeout,
            "success_threshold": self.success_threshold,
        }
    
    def reset(self):
        """Reset circuit breaker to initial state."""
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.half_open_request_count = 0
        self.last_failure_time = None
        self.last_success_time = None
        self.last_state_change = time.time()