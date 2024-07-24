// styles/theme.js
export const lightTheme = {
  colors: {
    primary: '#007bff',
    primaryHover: '#0056b3',
    background: '#ffffff',
    text: '#333333',
    border: '#cccccc',
  },
  fontSize: {
    small: '12px',
    medium: '16px',
    large: '20px',
  },
  breakpoints: {
    mobile: '768px',
  },
};

export const darkTheme = {
  colors: {
    primary: '#0a84ff',
    primaryHover: '#409cff',
    background: '#1c1c1e',
    text: '#ffffff',
    border: '#38383a',
  },
  fontSize: {
    small: '12px',
    medium: '16px',
    large: '20px',
  },
  breakpoints: {
    mobile: '768px',
  },
};

// styles/GlobalStyle.js
import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  body {
    font-family: 'Arial', sans-serif;
    background-color: ${props => props.theme.colors.background};
    color: ${props => props.theme.colors.text};
    margin: 0;
    padding: 0;
  }
`;

export default GlobalStyle;
