# Selenium Python DemoBlaze Test Suite

A comprehensive, production-ready test automation framework for the DemoBlaze e-commerce website built with Python, Selenium, and pytest.

## Key Features

### Advanced Architecture
- **Page Object Model (POM)** - Clean separation of test logic and page interactions
- **Centralized Locators** - All selectors organized in dedicated locator classes
- **Factory Pattern** - Flexible WebDriver initialization supporting Chrome, Firefox, and Edge
- **Modular Design** - Reusable components and utilities

### Robust Test Framework
- **Explicit Waits** - Smart element waiting strategies for flaky web applications
- **Alert Handling** - Automatic detection and dismissal of unexpected JavaScript alerts
- **Window Management** - Intelligent handling of new windows/tabs during navigation
- **Error Recovery** - Graceful handling of session timeouts and browser crashes

### Professional Reporting
- **Allure Integration** - Beautiful, detailed test reports with screenshots and logs
- **Structured Logging** - Step-by-step test execution tracking
- **Test Categorization** - Organized by features, stories, and severity levels

### Performance Optimized
- **Quick Test Suite** - 10 essential tests for rapid development cycles
- **Parallel Execution Ready** - Framework supports concurrent test runs
- **Resource Management** - Automatic cleanup of browser sessions

## Test Coverage

### Home Page Tests (6 tests)
- Page navigation and title verification
- Navigation elements presence validation
- Product display and information verification
- Footer elements and copyright text
- Modal functionality (login/signup)

### Product Page Tests (4 tests)
- Product details loading and verification
- Product image display validation
- Add to cart button functionality
- Navigation back to product listing

## Quick Start

### 1. Environment Setup
```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows PowerShell)
. .venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Quick Test Suite
```bash
pytest -q tests/test_home_page.py::TestHomePage::test_open_home_page \
  tests/test_home_page.py::TestHomePage::test_navigation_elements_present \
  tests/test_home_page.py::TestHomePage::test_products_are_displayed \
  tests/test_home_page.py::TestHomePage::test_product_information_displayed \
  tests/test_home_page.py::TestHomePage::test_footer_elements \
  tests/test_home_page.py::TestHomePage::test_modal_buttons_functional \
  tests/test_product_page.py::TestProductPage::test_product_details_displayed \
  tests/test_product_page.py::TestProductPage::test_product_image_displayed \
  tests/test_product_page.py::TestProductPage::test_add_to_cart_button_present \
  tests/test_product_page.py::TestProductPage::test_back_to_products_navigation
```

### 3. Generate Allure Report
```bash
pytest -q --alluredir=reports/allure
allure serve reports/allure
```

## Project Structure

```
selenium_python_resume_project/
├── pages/                 # Page Object classes
│   ├── home_page.py         # Home page interactions
│   ├── product_page.py      # Product page interactions
│   └── cart_page.py         # Cart page interactions
├── locators/             # Centralized element locators
│   ├── home_page_locators.py
│   ├── product_page_locators.py
│   └── cart_page_locators.py
├── helpers/              # Test utilities
│   ├── assertions.py        # Custom assertion methods
│   └── test_data.py         # Test data constants
├── utils/                # Framework utilities
│   └── driver_factory.py    # WebDriver initialization
├── tests/                # Test suites
│   ├── test_home_page.py    # Home page tests
│   └── test_product_page.py # Product page tests
├── reports/              # Test reports and screenshots
├── config.json              # Framework configuration
├── requirements.txt         # Python dependencies
└── pytest.ini              # Pytest configuration
```

## Configuration

### Browser Configuration (config.json)
```json
{
  "browser": "chrome",
  "base_url": "https://www.demoblaze.com",
  "headless": false,
  "implicit_wait": 10,
  "explicit_wait": 10,
  "page_load_timeout": 30
}
```

### Supported Browsers
- **Chrome** (default) - Most stable and recommended
- **Firefox** - Full compatibility
- **Edge** - Windows-specific support

## Advanced Features

### Smart Element Handling
```python
# Automatic retry on alert presence
element = self.find_element(locator)  # Handles unexpected alerts

# Intelligent window switching
self.switch_to_latest_window()  # Manages new windows/tabs

# Robust navigation
self.wait_for_url_contains("prod.html")  # URL-based page verification
```

### Custom Assertions
```python
# Rich assertion methods
Assertions.assert_text_contains(actual, expected)
Assertions.assert_list_not_empty(items)
Assertions.assert_greater_than(value, threshold)
```

### Page Object Methods
```python
# Clean, readable test code
home_page.open('https://www.demoblaze.com')
product_titles = home_page.get_product_titles()
home_page.click_product_by_name(first_product)
```

## Troubleshooting

### Common Issues
1. **Chrome Session Errors**
   - Update Chrome to latest version
   - Try headless mode: `"headless": true` in config.json
   - Check for conflicting Chrome instances

2. **Element Not Found**
   - Framework includes automatic retry logic
   - Check if DemoBlaze site structure changed
   - Verify network connectivity

3. **Allure Report Issues**
   - Install Allure CLI: `npm install -g allure-commandline`
   - Or remove `--alluredir` flag for basic pytest output

## Performance Metrics

- **Test Execution Time**: ~1.5 minutes for 10 tests
- **Success Rate**: 100% on stable DemoBlaze environment
- **Browser Memory Usage**: Optimized with automatic cleanup
- **Parallel Execution**: Ready for multi-threaded runs

## Learning Resources

This project demonstrates:
- **Selenium Best Practices** - Page Object Model, explicit waits, error handling
- **Python Testing** - pytest fixtures, parametrization, custom markers
- **Test Automation Architecture** - Modular design, configuration management
- **Professional Reporting** - Allure integration, structured logging

## Contributing

1. Fork the repository
2. Create feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit pull request

