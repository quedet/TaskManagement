/** @type {import('tailwindcss').Config} */
const Path = require('path');
const pwd = process.env.PWD;

const projectPaths = [
  Path.join(pwd, "./templates/**/*.html"),
]

const contentPaths = [...projectPaths]

module.exports = {
  content: contentPaths,
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms')
  ],
}
