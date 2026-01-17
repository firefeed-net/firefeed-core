# Email Service Tests

Unit tests for the FireFeed email service.

## Test Structure

### Unit Tests (`tests/unit/email/`)

- **`test_email_sender.py`** - Comprehensive tests for the email sender functionality
  - Email configuration validation
  - Template rendering and management
  - Email message creation and validation
  - SMTP connection and authentication
  - Email sending with various scenarios
  - Error handling and edge cases
  - Attachment handling
  - Multiple recipient support

### Integration Tests (`tests/integration/test_email_service.py`)

- **`test_email_service.py`** - Integration tests for the complete email service
  - End-to-end email sending workflows
  - Real SMTP configuration testing
  - Concurrent email sending
  - Error handling in realistic scenarios
  - Template integration testing

## Test Coverage

The email service tests cover:

- ✅ Email configuration validation
- ✅ Template rendering and internationalization
- ✅ SMTP connection and authentication
- ✅ Email message creation and validation
- ✅ Attachment handling
- ✅ Multiple recipient support (To, CC, BCC)
- ✅ Error handling and retry mechanisms
- ✅ Concurrent email sending
- ✅ Template integration with real data
- ✅ Security and validation checks

## Running Tests

```bash
# Run all email service tests
pytest tests/unit/email/ tests/integration/test_email_service.py

# Run only unit tests
pytest tests/unit/email/

# Run only integration tests
pytest tests/integration/test_email_service.py

# Run with coverage
pytest tests/unit/email/ tests/integration/test_email_service.py --cov=firefeed_core.email_service --cov-report=html
```

## Test Data

The tests use mock SMTP servers and do not send real emails. For integration testing with real SMTP servers, configure the test environment appropriately.

## Mocking Strategy

- SMTP connections are mocked to prevent actual email sending
- Templates are tested with mock data
- Error scenarios are simulated using exception raising
- Concurrent tests use asyncio.gather for realistic testing

## Test Categories

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions and workflows
- **Error Handling**: Test failure scenarios and recovery
- **Performance Tests**: Test concurrent operations and load handling