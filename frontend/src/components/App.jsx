import React from "react";
import { Fragment } from "react";

import Header from "./common/Header";
import Footer from "./common/Footer";
import AddTodo from "../containers/AddTodo";
import VisibleTodoList from "../containers/VisibleTodoList";

const App = () => (
    <Fragment>
        <Header />
        <AddTodo />
        <VisibleTodoList />
        <Footer />
    </Fragment>
);

export default App;
