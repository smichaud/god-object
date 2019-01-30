import React from "react";
import { render } from "react-dom";
import { createStore } from "redux";
import { Provider } from "react-redux";
import { MuiThemeProvider, createMuiTheme } from "@material-ui/core/styles";
import blue from "@material-ui/core/colors/blue";

import App from "./components/App";
import rootReducer from "./reducers";

// TODO: https://www.npmjs.com/package/connected-react-router
const store = createStore(rootReducer);
const theme = createMuiTheme({
    palette: {
        primary: blue,
    },
});

render(
    <Provider store={store}>
        <MuiThemeProvider theme={theme}>
            <App />
        </MuiThemeProvider>
    </Provider>,
    document.getElementById("root")
);
