🎨 juniorprint

"PyPI" (https://img.shields.io/pypi/v/juniorprint.svg)
"Python" (https://img.shields.io/pypi/pyversions/juniorprint.svg)
"License" (https://img.shields.io/pypi/l/juniorprint.svg)
"Build" (https://github.com/Tech-dax/Juniorprint/actions/workflows/publish.yml/badge.svg)

---

🚀 What is juniorprint?

"juniorprint" is a lightweight Python library that allows you to print colored and styled text in the terminal using a simple and readable syntax.

No need to remember ANSI escape codes anymore.

---

📦 Installation

Install via pip:

pip install juniorprint

---

⚡ Quick Start

from juniorprint import print_

print_("r_[Error] g_[Success] normal text")

---

🎯 How it works

You write text using this pattern:

<code>_[your text]

Example:

print_("r_[This is red]")

---

🎨 Available Styles

Code| Meaning
r| Red
g| Green
y| Yellow
b| Blue
m| Magenta
c| Cyan
w| White
d| Bold

You can combine them:

print_("rd_[Bold Red Text]")

---

📚 Examples

🔴 Basic Colors

from juniorprint import print_

print_("r_[Error]")
print_("g_[Success]")
print_("y_[Warning]")
print_("b_[Information]")

---

🎨 Mixed Text

print_("r_[Error:] File not found")
print_("g_[OK:] Operation completed")

---

💪 Bold Text

print_("d_[Bold text]")
print_("rd_[Critical Error]")

---

🔥 Multiple Styles in One Line

print_("g_[OK] r_[Error] y_[Warning] b_[Info]")

---

🧠 Dynamic Example

name = "Alice"
status = "online"

print_(f"g_[User] {name} is {status}")

---

💡 Mixing Styled and Normal Text

print_("Normal text g_[green text] back to normal r_[red text]")

---

🛠️ Why use juniorprint?

- Simple and readable syntax
- No need to remember ANSI codes
- Lightweight and fast
- Works with standard Python

---

📁 Project Structure

juniorprint/
├── juniorprint/
│   ├── printer.py
│   ├── formatter.py
│   └── styles.py
├── examples/
│   └── demo.py

---

🌍 Source Code

GitHub repository:
https://github.com/Tech-dax/Juniorprint

---

📜 License

MIT License

---

⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!