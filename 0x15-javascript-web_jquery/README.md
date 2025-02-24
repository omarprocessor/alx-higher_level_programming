# 0x15. JavaScript - Web jQuery

## Front-end | JavaScript

### Project Duration
**Start Date:** February 19, 2025, 6:00 AM  
**Deadline:** February 25, 2025, 6:00 AM  
**Manual QA review required** (request it upon completion)

---

## Concepts
This project covers the following concepts:
- JavaScript in the browser
- Dealing with data statically vs. dynamically

---

## Resources
Read or watch:
- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction)
- [Selector](https://api.jquery.com/category/selectors/)
- [Get and set content](https://api.jquery.com/html/)
- [Manipulate CSS classes](https://api.jquery.com/addClass/)
- [Manipulate DOM elements](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [API Introduction](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
- [GET & POST requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [JQuery Ajax Tutorial](https://www.youtube.com/watch?v=fEYx8dQr_cQ)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
- [JQuery](https://jquery.com/)
- [JQuery API](https://api.jquery.com/)
- [JQuery Ajax](https://api.jquery.com/jquery.ajax/)

---

## Learning Objectives
By the end of this project, you should be able to explain:
- Why JQuery makes front-end programming easier
- How to select HTML elements using JavaScript
- How to select HTML elements using JQuery
- Differences between ID, class, and tag name selectors
- How to modify an HTML element's style
- How to get and update HTML element content
- How to manipulate the DOM
- How to make a GET request with JQuery Ajax
- How to make a POST request with JQuery Ajax
- How to listen/bind to DOM events
- How to listen/bind to user events

---

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- Files interpreted on **Chrome version 57.0**
- Files must end with a **new line**
- **A `README.md` file at the root directory is mandatory**
- Code must be **semistandard compliant** (`semistandard *.js --global $`)
- Must use **JQuery version 3.x**
- **`var` is not allowed** (use `const` or `let` instead)
- **HTML should not reload for each action** (use DOM manipulation)

---

## Importing JQuery
```html
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

---

## Manual QA Review
- Request a **peer review** before the project deadline
- If no peer reviews are available, request a review from a TA or staff member

---

## Repository
- **GitHub Repository:** `alx-higher_level_programming`
- **Directory:** `0x15-javascript-web_jquery`

---

## Tasks Overview

### 0. No JQuery
- **File:** `0-script.js`
- Update `<header>` text color to **red (#FF0000)** using `document.querySelector`.
- **Do not use JQuery**.

### 1. With JQuery
- **File:** `1-script.js`
- Update `<header>` text color to **red (#FF0000)** using JQuery.

### 2. Click and Turn Red
- **File:** `2-script.js`
- Change `<header>` text color to **red (#FF0000)** when `DIV#red_header` is clicked.
- **Use JQuery API**.

### 3. Add `.red` Class
- **File:** `3-script.js`
- Add the class `red` to `<header>` when `DIV#red_header` is clicked.

### 4. Toggle Classes
- **File:** `4-script.js`
- Toggle `<header>` between `red` and `green` classes when `DIV#toggle_header` is clicked.

### 5. List of Elements
- **File:** `5-script.js`
- Add a new `<li>Item</li>` to `UL.my_list` when `DIV#add_item` is clicked.

... *(additional tasks follow the same format)* ...

---

## Author
**[Your Name]**  
*ALX Software Engineering Cohort*

---
