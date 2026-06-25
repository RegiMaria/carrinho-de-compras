# 🛒 Shopping Cart - SOLID Study Project

A Python project to study the **Single Responsibility Principle (SRP)**, the first principle of SOLID.

---

## What is SOLID?

SOLID is a set of five principles for writing clean, organized, and maintainable code.

| Letter | Principle | Idea |
|--------|-----------|------|
| **S** | Single Responsibility | Each class has **one** responsibility |
| **O** | Open/Closed | Open for extension, closed for modification |
| **L** | Liskov Substitution | Subclasses can replace their parent class |
| **I** | Interface Segregation | Small and specific interfaces |
| **D** | Dependency Inversion | Depend on abstractions, not implementations |

This project focuses on the **S — Single Responsibility Principle**.

---

## Project Structure

```
carrinho-de-compras/
│
├── src/
│   ├── carrinho_sem_srp.py   ← without SRP (one class does everything)
│   └── carrinho_com_srp.py   ← with SRP (responsibilities separated)
│
├── index.py                  ← local web server (view in browser)
└── README.md
```

---

## Files

### `carrinho_sem_srp.py`
One single class `CarrinhoCompra` handles everything:
- Manages items and total value
- Validates the cart
- Sends confirmation email
- Confirms the order

**Problem:** if you need to change the email logic, you have to touch the same class that manages items. This creates risk of breaking things.

### `carrinho_com_srp.py`
Each class has one single responsibility.



### `index.py`
A simple local web server. Run it and open the browser to see the cart working.

---

## How to Run

### Option 1 - Run in the terminal

```bash
# without SRP
python3 src/carrinho_sem_srp.py

# with SRP
python3 src/carrinho_com_srp.py
```

### Option 2 - Run in the browser

```bash
python3 index.py
```

Then open your browser at:
```
http://localhost:8000
```

---

## Requirements

- Python 3.10 or higher
- No external libraries needed

---

## Key Concepts for Beginners

| Concept | Meaning |
|---------|---------|
| **Class** | A blueprint to create objects |
| **Attribute** | Data that the object stores (`self.items`) |
| **Method** | Action that the object can do (`def add_item`) |
| **Instance** | An object created from a class (`CarrinhoCompra()`) |
| **`self`** | Reference to the object itself inside the class |
| **`__init__`** | Constructor — runs automatically when object is created |
| **Dictionary** | Key-value structure (`{"item": "TV", "value": 3570.25}`) |
| **`if __name__ == "__main__"`** | Block that runs only when the file is executed directly |

---

## References

1.[Agile Software Development](https://sites.google.com/site/unclebobconsultingllc/getting-a-solid-start): Principles, Patterns, and Practices - Uncle Bob
2. [Clean Code(PT)](https://www.amazon.com.br/C%C3%B3digo-limpo-Robert-C-Martin/dp/8576082675/ref=sr_1_1_sspa?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=29P73QU0D2HGB&dib=eyJ2IjoiMSJ9.uqzFlAdb2__fCzeNdE3yfINuHBwVXD9B2YRU9wA4j-DJsSA_9ESEtIT3RfBmZXDwJ1mKkQfqbFdyk-QmMdtCYpMfleGTvKNPe3vBfiUxcjoWggJRbw2p7D0OmSxtfob42pdBV6YV9kbAL6i3CD-GiJLHTjNtkpiLdBJfygU_hTtEN0PlSihjdpIhv_uUdpWLd8j8vAE6zVxC3qDBz5w4VVkf-tbDExbNcCP7CfU_vjc.VkUVtibe-pNcQXkioP6Nxc85EXayBMTEjt3LtFYtyMM&dib_tag=se&keywords=clean+code&qid=1782390349&s=books&sprefix=clean+cod%2Cstripbooks%2C215&sr=1-1-spons&ufe=app_do%3Aamzn1.fos.b07885ca-1112-4aa2-9643-2c998a360229&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1) - Robert C. Martin (Uncle Bob)

---

✨*Happy coding! The best way to learn is to type the code, not copy and paste.* ✨