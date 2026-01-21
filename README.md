# SmartHealth - AI-Based Healthcare Platform


## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [File Directory & Functionalities](#file-directory--functionalities)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [Database Schema](#database-schema)
- [Module Documentation](#module-documentation)
- [Contributing Guidelines](#contributing-guidelines)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [Testing](#testing)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Contact & Support](#contact--support)

---

## 🎯 Project Overview

**SmartHealth** is an AI-powered comprehensive healthcare platform designed to provide personalized health monitoring, medical guidance, medication management, and doctor consultation services. The platform combines modern web design with robust backend functionality to deliver a seamless user experience.

---

## ✨ Features

### 🔐 **Module 1: Authentication & User Profile**
- User registration and login system
- Secure password management
- Health profile creation and management
- Personal health history tracking

### 🍽️ **Module 2: Diet & Nutrition**
- Personalized diet recommendations
- Nutrition database with calorie tracking
- Food categorization (Vegan, Vegetarian, Non-veg, etc.)
- Meal timing suggestions

### 🩺 **Module 3: Symptom Analysis**
- AI-powered symptom checker
- Disease prediction based on symptoms
- OTC medicine recommendations
- Severity assessment

### 💊 **Module 4: Medicine & Pharmacy**
- Medicine reminder system with notifications
- Medicine dosage information
- Drug interaction warnings
- Local pharmacy availability checking
- Pharmacy locator with contact information

### 👨‍⚕️ **Module 5: Doctor Consultation & Health Monitoring**
- Doctor directory with specialization filtering
- Online consultation booking
- Health metric tracking (weight, BP, etc.)
- Emergency alert system
- Real-time health monitoring

### 🎨 **UI/UX Features**
- Modern, responsive design
- Dark/Light mode toggle
- Intelligent navbar with active section highlighting
- Smooth animations and transitions
- Mobile-first approach
- Glassmorphism effects
- Professional gradient design

---

## 📁 Project Structure

```
smart health pharm medicine/
├── app.py                          # Main Flask application
├── database.db                     # SQLite database (auto-created)
├── database.sqbpro                 # SQLite database project file
├── README.md                       # Project documentation (this file)
├── EXECUTIVE_SUMMARY.md            # Executive overview
├── 00_READ_ME_FIRST.md             # Quick start guide
├── REQUIREMENTS_CHECKLIST.md       # Project requirements tracking
├── IMPLEMENTATION_CHECKLIST.md     # Implementation tracking
├── FILE_MANIFEST.md                # Complete file listing
├── DESIGN_SHOWCASE.md              # UI/UX design documentation
├── NAVBAR_QUICK_REFERENCE.md       # Navbar implementation guide
├── UI_UPDATE_GUIDE.md              # UI update instructions
├── UI_QUICK_REFERENCE.md           # UI quick reference
├── NAVBAR_CSS_ONLY.css             # Navbar styling
│
├── templates/                      # HTML templates
│   ├── home.html                   # Landing page with hero section
│   ├── login.html                  # User login page
│   ├── register.html               # User registration page
│   ├── dashboard.html              # User dashboard with stats
│   ├── profile.html                # User profile management
│   ├── navbar.html                 # Reusable navbar component
│   ├── diet.html                   # Diet & nutrition module
│   ├── medicines.html              # Medicine reminder module
│   ├── module3.html                # Symptom analysis module
│   ├── pharmacy.html               # Pharmacy locator module
│   ├── consultation.html           # Doctor consultation module
│   ├── admin_login.html            # Admin login page
│   └── admin_dashboard.html        # Admin dashboard
│
├── static/                         # Static files
│   └── dashboard_img.png           # Dashboard hero image
│
└── datasets/                       # CSV datasets
    ├── module2/
    │   └── diet_dataset.csv        # Nutrition database
    ├── module3/
    │   └── symptom_medicine_dataset.csv    # Symptoms & medicines
    ├── module4/
    │   ├── medicine_pharmacy_dataset.csv   # Medicine data
    │   └── pharmacy_availability_dataset.csv # Pharmacy info
    └── module5/
        ├── doctor_consultation_dataset.csv # Doctor directory
        └── health_monitoring_dataset.csv   # Health monitoring data
```

---

## 📂 File Directory & Functionalities

### **Backend Files**

| File | Location | Functionality | Key Functions |
|------|----------|---------------|----------------|
| **app.py** | Root | Main Flask application & routing | init_db(), insert_dummy_data(), all route handlers |
| **database.db** | Root | SQLite database with all tables | Auto-created on first run |

### **Frontend - Templates**

| Template | Purpose | Features |
|----------|---------|----------|
| **home.html** | Landing page | Hero section, Features (6 cards), Modules (5 cards), CTA, Footer |
| **login.html** | User authentication | Login form, Validation, Navbar, Dark mode |
| **register.html** | User registration | Registration form, Password strength, Navbar, Dark mode |
| **dashboard.html** | User dashboard | Quick stats, Module shortcuts, Health overview, Navbar |
| **profile.html** | User profile | Profile management, Health info editing |
| **navbar.html** | Navigation component | Reusable navbar structure, Active highlighting |
| **diet.html** | Module 2 | Diet recommendations, Food database, Calorie tracker |
| **medicines.html** | Module 4 | Medicine reminders, Dosage info, Drug interactions |
| **module3.html** | Module 3 | Symptom checker, Disease prediction, Medicine suggestions |
| **pharmacy.html** | Module 4 | Pharmacy locator, Medicine availability, Contact info |
| **consultation.html** | Module 5 | Doctor directory, Consultation booking, Appointment tracking |
| **admin_login.html** | Admin panel | Admin authentication |
| **admin_dashboard.html** | Admin panel | Admin controls & analytics |

### **Static Files**

| File | Purpose |
|------|---------|
| **dashboard_img.png** | Hero image for dashboard |

### **Datasets (CSV)**

| File | Module | Contains |
|------|--------|----------|
| **diet_dataset.csv** | Module 2 | Food items, calories, nutrients, diet types |
| **symptom_medicine_dataset.csv** | Module 3 | Symptoms, severity, possible conditions, medicines |
| **medicine_pharmacy_dataset.csv** | Module 4 | Medicine names, dosages, types, interactions |
| **pharmacy_availability_dataset.csv** | Module 4 | Pharmacy details, locations, medicine stock |
| **doctor_consultation_dataset.csv** | Module 5 | Doctor profiles, specialization, availability |
| **health_monitoring_dataset.csv** | Module 5 | Health records, metrics, alerts |

---

## 🛠️ Tech Stack

### **Backend**
- **Framework:** Flask 2.x
- **Database:** SQLite3
- **Language:** Python 3.8+

### **Frontend**
- **Markup:** HTML5
- **Styling:** CSS3 (with CSS Variables, Flexbox, Grid)
- **Scripting:** Vanilla JavaScript (ES6+)
- **Icons:** Font Awesome 6.4.0
- **Design Pattern:** Responsive Mobile-First

### **Additional Tools**
- Version Control: Git
- Database GUI: SQLite Browser (optional)

---

## 🚀 Getting Started

### Prerequisites

Before setting up the project, ensure you have:

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Any text editor or IDE (VS Code recommended)

### System Requirements

- **OS:** Windows, macOS, or Linux
- **RAM:** 512 MB minimum
- **Storage:** 100 MB free space
- **Internet:** For downloading dependencies

---

## 📦 Installation & Setup

### Step 1: Clone or Download the Project

```bash
git clone <repository-url>
cd smart\ health\ pharm\ medicine
```

Or download the ZIP and extract it.

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install flask sqlite3
```

Or if using requirements.txt:

```bash
pip install -r requirements.txt
```

### Step 4: Navigate to Project Directory

```bash
cd smart\ health\ pharm\ medicine
```

---

## ▶️ Running the Application

### Start the Flask Server

```bash
python app.py
```

Expected output:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

### Access the Application

Open your browser and navigate to:
```
http://localhost:5000
```

### First Time Setup

1. The application will auto-create `database.db`
2. Dummy data will be inserted automatically
3. Default test credentials:
   - Username: `user1` | Password: `pass123`
   - Username: `user2` | Password: `pass456`

---

## 🗄️ Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
)
```

### Health Profile Table
```sql
CREATE TABLE health_profile (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    age INTEGER,
    gender TEXT,
    height REAL,
    weight REAL,
    activity TEXT,
    diseases TEXT,
    allergies TEXT,
    medicines TEXT
)
```

### Module 2: Diet & Nutrition
```sql
CREATE TABLE diet_nutrition_dataset (
    food_id INTEGER PRIMARY KEY,
    food_name TEXT,
    category TEXT,
    calories INTEGER,
    protein INTEGER,
    carbs INTEGER,
    fats INTEGER,
    diet_type TEXT,
    recommended_time TEXT
)
```

### Module 3: Symptom Analysis
```sql
CREATE TABLE symptom_medicine_dataset (
    symptom_id INTEGER PRIMARY KEY,
    symptom_name TEXT,
    severity TEXT,
    duration_days INTEGER,
    possible_condition TEXT,
    otc_medicine TEXT,
    medicine_type TEXT,
    dosage_info TEXT,
    doctor_consult TEXT,
    notes TEXT
)
```

### Module 4: Medicine Reminder
```sql
CREATE TABLE medicine_reminder_dataset (
    medicine_id INTEGER PRIMARY KEY,
    medicine_name TEXT,
    dosage TEXT,
    frequency TEXT,
    duration_days INTEGER,
    reminder_time TEXT,
    medicine_type TEXT,
    interaction_warning TEXT
)
```

### Module 4: Pharmacy Availability
```sql
CREATE TABLE pharmacy_availability_dataset (
    pharmacy_id INTEGER PRIMARY KEY,
    pharmacy_name TEXT,
    location TEXT,
    medicine_name TEXT,
    stock TEXT,
    contact TEXT
)
```

### Module 5: Doctor Consultation
```sql
CREATE TABLE doctor_consultation_dataset (
    doctor_id INTEGER PRIMARY KEY,
    doctor_name TEXT,
    specialization TEXT,
    hospital_name TEXT,
    location TEXT,
    contact TEXT,
    consultation_type TEXT,
    availability TEXT
)
```

### Module 5: Health Monitoring
```sql
CREATE TABLE health_monitoring_dataset (
    record_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    weight REAL,
    symptom TEXT,
    severity TEXT,
    days_persisted INTEGER,
    doctor_alert TEXT,
    emergency_flag TEXT,
    remarks TEXT
)
```

---

##  Module Documentation

### Module 1: Authentication & User Profile
- **Location:** `login.html`, `register.html`, `profile.html`
- **Database:** users, health_profile tables
- **Functionality:** User registration, login, profile creation
- **Key Features:** Session management, data validation

### Module 2: Diet & Nutrition
- **Location:** `diet.html`
- **Dataset:** `datasets/module2/diet_dataset.csv`
- **Functionality:** Personalized diet recommendations based on health profile
- **Key Features:** Calorie tracking, food categorization, meal planning

### Module 3: Symptom Analysis
- **Location:** `module3.html`
- **Dataset:** `datasets/module3/symptom_medicine_dataset.csv`
- **Functionality:** AI-powered symptom checker and condition prediction
- **Key Features:** OTC medicine recommendations, severity assessment

### Module 4: Medicine & Pharmacy
- **Location:** `medicines.html`, `pharmacy.html`
- **Datasets:** `medicine_pharmacy_dataset.csv`, `pharmacy_availability_dataset.csv`
- **Functionality:** Medicine reminders, pharmacy locator, medicine tracking
- **Key Features:** Drug interaction warnings, availability checking, location services

### Module 5: Doctor Consultation & Health Monitoring
- **Location:** `consultation.html`
- **Datasets:** `doctor_consultation_dataset.csv`, `health_monitoring_dataset.csv`
- **Functionality:** Doctor directory, consultation booking, health monitoring
- **Key Features:** Emergency alerts, health tracking, specialist filtering

---

## 🤝 Contributing Guidelines

We welcome contributions! Please follow these guidelines to maintain code quality and consistency.

### How to Contribute

1. **Fork the Repository**
   ```bash
   git clone <your-fork-url>
   cd smart\ health\ pharm\ medicine
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow code standards (see below)
   - Keep commits focused and atomic
   - Update documentation as needed

4. **Test Your Changes**
   - Run the application locally
   - Test all affected modules
   - Check for console errors

5. **Commit & Push**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Provide clear description of changes
   - Reference any related issues
   - Include testing information

### Types of Contributions Welcome

- 🐛 **Bug Fixes:** Report and fix bugs
- ✨ **New Features:** Add new functionality
- 📖 **Documentation:** Improve docs and guides
- 🎨 **UI/UX Improvements:** Enhance interface
- ⚡ **Performance:** Optimize code and database
- 🧪 **Tests:** Add unit and integration tests

---

##  Development Workflow

### Setting Up Development Environment

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

2. **Activate Virtual Environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Development Dependencies**
   ```bash
   pip install flask
   pip install pytest  # for testing
   ```

4. **Create `.env` for Configuration** (Optional)
   ```
   FLASK_ENV=development
   FLASK_DEBUG=True
   SECRET_KEY=your-secret-key
   ```

### Development Server

Run in debug mode:
```bash
python app.py
```

Changes will auto-reload (if debug mode enabled).

### Branch Naming Convention

- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring
- `test/description` - Test additions

---

##  Code Standards

### Python Code Style

- Follow **PEP 8** guidelines
- Use meaningful variable names
- Add docstrings for functions
- Max line length: 100 characters
- Use type hints where applicable

Example:
```python
def get_user_profile(user_id: int) -> dict:
    """
    Retrieve user profile from database.
    
    Args:
        user_id (int): The user's unique identifier
        
    Returns:
        dict: User profile information
    """
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM health_profile WHERE user_id=?", (user_id,))
    profile = cur.fetchone()
    con.close()
    return profile
```

### HTML/CSS Standards

- Use semantic HTML5 elements
- Use CSS classes with meaningful names
- Maintain responsive design (mobile-first)
- Use CSS variables for colors and sizes
- Comment complex CSS blocks

Example:
```html
<!-- Semantic HTML -->
<section class="module-container">
    <article class="feature-card">
        <h2 class="feature-title">Feature Name</h2>
        <p class="feature-description">Description</p>
    </article>
</section>
```

### JavaScript Standards

- Use vanilla JavaScript or ES6+
- Use descriptive function names
- Add comments for complex logic
- Handle errors gracefully
- Avoid global variables

Example:
```javascript
function toggleDarkMode() {
    const isDarkMode = localStorage.getItem('darkMode') === 'true';
    const newDarkMode = !isDarkMode;
    localStorage.setItem('darkMode', newDarkMode);
    applyTheme(newDarkMode);
}
```

---

##  Testing

### Manual Testing Checklist

Before submitting changes:

- [ ] Application starts without errors
- [ ] Login functionality works
- [ ] All modules load correctly
- [ ] Navigation works properly
- [ ] Responsive design on mobile/tablet/desktop
- [ ] Dark mode toggle works
- [ ] Database operations function correctly
- [ ] No console errors

### Testing Commands

```bash
# Run the application
python app.py

# Check for syntax errors
python -m py_compile app.py

# Run with verbose logging (if configured)
python app.py --verbose
```

### Automated Testing Setup (Future)

To add pytest tests:

```bash
pip install pytest
pytest tests/
```

---

##  Deployment

### Before Deployment

1. **Set Debug Mode to False**
   ```python
   app.debug = False
   ```

2. **Use Strong Secret Key**
   ```python
   app.secret_key = "your-very-secure-random-key"
   ```

3. **Configure Database Path**
   ```python
   DB_NAME = "path/to/production/database.db"
   ```

4. **Test in Production Mode**
   ```bash
   python app.py
   ```

### Deployment Options

#### Option 1: Heroku
```bash
git init
heroku create your-app-name
git push heroku main
```

#### Option 2: PythonAnywhere
1. Create account at pythonanywhere.com
2. Upload files
3. Configure web app
4. Set WSGI file

#### Option 3: Self-Hosted Server
```bash
# Install gunicorn (production server)
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### Option 4: Docker
Create `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:**
```bash
pip install flask
```

#### Issue: "Port 5000 already in use"
**Solution:**
```bash
# Windows
netstat -ano | findstr :5000

# macOS/Linux
lsof -i :5000

# Then run on different port
python app.py --port 5001
```

#### Issue: Database not created
**Solution:**
- Delete `database.db` if exists
- Restart the application
- Check write permissions on directory

#### Issue: CSS/JavaScript not loading
**Solution:**
- Clear browser cache (Ctrl+Shift+Delete)
- Check file paths in templates
- Verify `static` folder exists
- Check browser console for 404 errors

#### Issue: Dark mode not persisting
**Solution:**
- Check if localStorage is enabled
- Clear browser data
- Check browser console for JS errors

### Debug Mode

Enable detailed error messages:

```python
# In app.py
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Log Files

Check for error logs:
```bash
# If logging is configured
tail -f logs/app.log
```

---

## 📞 Contact & Support

### Getting Help

- **Documentation:** Check `README.md`
- **Quick Reference:** See `NAVBAR_QUICK_REFERENCE.md`
- **Issues:** Create an issue on GitHub
- **Email:** y22cs029@rvrjc.ac.in



### Reporting Issues

When reporting bugs, include:
1. **Description:** What's the problem?
2. **Steps:** How to reproduce it?
3. **Expected:** What should happen?
4. **Actual:** What actually happens?
5. **Environment:** Python version, OS, browser
6. **Screenshots:** If applicable

---

## 📜 License

This project is licensed under the **MIT License** - see LICENSE file for details.

---

## 🎉 Acknowledgments

- Font Awesome for icons
- Flask community for excellent framework
- Contributors and testers
- Medical data providers
---

## Commit Message Format

Use clear, descriptive commit messages:

```
feat: add new feature description
fix: fix bug description
docs: update documentation
style: code formatting changes
refactor: code restructuring
test: add or update tests
chore: maintenance tasks
```

Example:
```bash
git commit -m "feat: add dark mode toggle to navbar"
git commit -m "fix: resolve database connection timeout issue"
git commit -m "docs: update README with deployment instructions"
```

---

## 🎯 Next Steps

1. **Read:** `READ_ME.md` for quick start
2. **Setup:** Follow installation instructions
3. **Explore:** Check each module's functionality
4. **Contribute:** Follow contributing guidelines
5. **Test:** Use testing checklist
6. **Deploy:** When ready, follow deployment guide

---

**Happy Contributing! 🚀**

*Last Updated: January 21, 2026*

