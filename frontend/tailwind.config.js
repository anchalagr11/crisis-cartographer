/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        crisis: {
          primary: '#1a365d',
          secondary: '#2d3748',
          accent: '#38b2ac',
        }
      }
    },
  },
  plugins: [],
}
