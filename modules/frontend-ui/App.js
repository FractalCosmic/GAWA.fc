// App.js
import React, { useState } from 'react';
import { ThemeProvider } from 'styled-components';
import { Provider } from 'react-redux';
import { lightTheme, darkTheme } from './styles/theme';
import GlobalStyle from './styles/GlobalStyle';
import { store } from './store';
import Button from './components/Button';
import Input from './components/Input';
import ContributionDashboard from './components/ContributionDashboard';

const App = () => {
  const [isDarkMode, setIsDarkMode] = useState(false);

  return (
    <Provider store={store}>
      <ThemeProvider theme={isDarkMode ? darkTheme : lightTheme}>
        <GlobalStyle />
        <div>
          <Button onClick={() => setIsDarkMode(!isDarkMode)}>
            Toggle Theme
          </Button>
          <Input placeholder="Search..." />
          <ContributionDashboard />
        </div>
      </ThemeProvider>
    </Provider>
  );
};

export default App;
