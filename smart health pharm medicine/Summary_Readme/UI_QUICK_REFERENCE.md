# SmartHealth UI - Quick Reference Guide

## 🎨 Visual Design System

### Color Palette
```
Primary Blue:    #6366f1
Purple:          #8b5cf6
Gradient:        135deg, #6366f1 → #8b5cf6
Dark Background: #1a1a1a
Text Dark:       #1f2937
Text Light:      #6b7280
Light BG:        #f9fafb
```

### Typography
- Font Family: Segoe UI, Tahoma, Geneva, Verdana, sans-serif
- Hero Title: 64px, weight 900
- Section Title: 42px, weight 900
- Card Header: 20px, weight 700
- Body: 14px-18px

### Spacing System
- Navbar Height: 70px (mobile: 60px)
- Section Padding: 100px top/bottom (mobile: 60px)
- Card Padding: 45px 30px (mobile: 25px 15px)
- Grid Gap: 25-30px (mobile: 20px)

---

## 📱 Responsive Breakpoints

### Desktop (1024px+)
- Full width layouts
- All features visible
- 3-column feature grid
- Hero side-by-side

### Tablet (768px-1023px)
- Adjusted padding (30px)
- Feature grid responsive
- Navbar optimized
- Stacked where needed

### Mobile (480px-767px)
- Single column layouts
- Reduced padding (20px)
- Hamburger-friendly
- Full-width cards

### Small Mobile (<480px)
- Extra compact
- Single feature per row
- Minimal padding
- Stacked buttons

---

## 🎯 Features Overview

### 1. Active Navbar Link Highlighting
**How it Works:**
- Scroll detection monitors section positions
- When section enters viewport, navbar link highlights
- Gradient underline animation (0 → 60% width)
- Color changes to primary blue (#6366f1)

**User Experience:**
- Click navbar link → smooth scroll to section
- As you scroll → link automatically highlights
- Visual feedback for current location

### 2. Service Cards (5 Total)
**Layout:** Responsive grid with auto-fit
**Design Elements:**
- Top border: 5px gradient line
- Hover: -12px lift with enhanced shadow
- Icon: 55px, scales 1.15x on hover
- Background: White with subtle hover effect
- Transition: 0.35s cubic-bezier for smooth animation

**Spacing:**
- Desktop: 5 columns equal width
- Tablet: 3-4 columns
- Mobile: 2 columns or single

### 3. Feature Cards (6 Total)
**Layout:** 3 columns (desktop), responsive on smaller screens
**Design Elements:**
- Left border: 5px gradient accent
- Background: Subtle gradient (f8f9ff → faf5ff)
- Icon: 45px, scales 1.2x on hover
- Decorative circle: Animates on hover
- Hover: -10px lift with shadow

**Special Feature:** Animated background circle (100px) that moves on hover

### 4. Dark Mode
**Activation:** Click moon icon in navbar
**Persistence:** Saved to localStorage
**Icon Change:** Moon → Sun when active

**Dark Colors:**
- Background: #1a1a1a
- Cards: #2d2d2d (services) / #1f1f1f (features)
- Text Primary: #e0e0e0
- Text Secondary: #b0b0b0
- Navbar: rgba(30, 30, 30, 0.95)

### 5. Dashboard Header
**Layout:** Two-column flexbox
**Left Column:**
- Title: "Your Health Profile"
- Description text
- Icon: Chart-line

**Right Column:**
- Healthcare illustration (image)
- Max-width: 300px (desktop), 200px (mobile)
- Responsive scaling

**Responsive:** Stacks vertically on mobile (flex-direction: column)

---

## 🎬 Animations

### slideInLeft
```
Duration: 0.8s
From: opacity 0, translateX(-40px)
To: opacity 1, translateX(0)
Used: Hero content, buttons
```

### slideInRight
```
Duration: 0.8s
From: opacity 0, translateX(40px)
To: opacity 1, translateX(0)
Used: Hero image
```

### fadeInUp
```
Duration: 0.8s
From: opacity 0, translateY(30px)
To: opacity 1, translateY(0)
Used: Section titles, cards
Stagger: 0.2s, 0.4s delays
```

### Hover Transforms
- Service Card: translateY(-12px)
- Feature Card: translateY(-10px)
- Icon: scale(1.15) rotate(10deg) for services
- Icon: scale(1.2) for features

---

## 🔧 JavaScript Functions

### Dark Mode Toggle
```javascript
function toggleDarkMode() {
    body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', 'true/false');
    updateIcon(); // moon ↔ sun
}
```

### Scroll Detection
```javascript
window.addEventListener('scroll', () => {
    // Detect current section
    // Update navbar active link
    // Remove from others
});
```

### Smooth Scrolling
```javascript
a[href^="#"].addEventListener('click', (e) => {
    e.preventDefault();
    target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
});
```

### Module Navigation
```javascript
function goModule1() { window.location.href = "/register"; }
function goDiet() { window.location.href = "/diet"; }
// etc...
```

---

## 📊 Grid Specifications

### Services Grid
- Columns: `repeat(auto-fit, minmax(220px, 1fr))`
- Gap: 25px
- Min-width: 220px per card
- Total Desktop: 5 columns

### Features Grid
- Columns: `repeat(auto-fit, minmax(280px, 1fr))`
- Gap: 30px
- Min-width: 280px per card
- Total Desktop: 3 columns

### Dashboard Header
- Display: flex
- Align: center
- Gap: 40px
- Mobile: flex-direction column, gap 20px

---

## 🎨 Hover Effects

### Service Card Hover
```css
transform: translateY(-12px);
box-shadow: 0 20px 50px rgba(99, 102, 241, 0.2);
icon: scale(1.15) rotate(10deg);
```

### Feature Card Hover
```css
transform: translateY(-10px);
box-shadow: 0 15px 40px rgba(99, 102, 241, 0.15);
background: linear-gradient(135deg, #f0f2ff, #f5f0ff);
icon: scale(1.2);
circle: translate(0, 0); // animate in
```

### Navbar Link Hover
```css
color: #6366f1;
underline: 0 → 60% width (gradient);
```

### Button Hover
```css
.btn-primary: translateY(-3px);
box-shadow: enhanced;

.btn-secondary: 
background: white;
color: primary;
```

---

## 📐 Box Shadows

### Subtle
```css
box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
```

### Medium
```css
box-shadow: 0 5px 25px rgba(0, 0, 0, 0.08);
```

### Enhanced on Hover
```css
box-shadow: 0 20px 50px rgba(99, 102, 241, 0.2);
```

### Dark Mode
```css
box-shadow: 0 5px 25px rgba(0, 0, 0, 0.4);
```

---

## 🎯 Navigation Structure

```
Navbar (fixed, z-index: 1000)
├── Brand (left): SmartHealth logo
├── Menu (center): 
│   ├── Home → #home
│   ├── Services → #services
│   ├── Features → #features
│   ├── About → #about
│   └── Login/Register → /login
└── Icons (right):
    ├── Dark mode toggle
    └── (Auth button on other pages)
```

---

## ✅ Compliance Checklist

- ✅ Navbar links with equal spacing
- ✅ "Services" instead of "Modules"
- ✅ Active link highlighting on scroll
- ✅ Color & underline on active state
- ✅ Remove "Get Started" button
- ✅ Services properly arranged (no gaps)
- ✅ Features properly arranged (no gaps)
- ✅ Dark mode on entire page
- ✅ Healthcare illustration support
- ✅ Responsive design (all breakpoints)
- ✅ Smooth animations
- ✅ Professional appearance

---

**Last Updated**: 2026  
**Version**: 2.0 - Modernization Complete
