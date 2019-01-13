import React from "react";
import { connect } from "react-redux";
import Button from "@material-ui/core/Button";
import Input from "@material-ui/core/Input";

import { addTodo } from "../actions";

const AddTodo = ({ dispatch }) => {
    let input;

    return (
        <div>
            <form
                onSubmit={(e) => {
                    e.preventDefault();
                    if (!input.value.trim()) {
                        return;
                    }
                    dispatch(addTodo(input.value));
                    input.value = "";
                }}
            >
                <Input ref={(node) => (input = node)} />
                <Button type="submit" variant="contained" color="primary">
                    Add todo
                </Button>
            </form>
        </div>
    );
};

export default connect()(AddTodo);
