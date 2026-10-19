## 2024-05-14 - Active State Navigation Accessibility
**Learning:** In static sites with multiple language versions and separate pages for each section (like Contact), relying purely on a `.activo` CSS class for the current menu item leaves screen reader users without context about their current location. The visual styling is there, but the semantic meaning is missing.
**Action:** Always pair visual active states (like `.activo` or similar classes) with `aria-current="page"` on navigation links and language switchers to ensure parity between the visual and accessible experiences.
