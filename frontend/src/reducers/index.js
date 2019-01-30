import { combineReducers } from "redux";
import todos from "./todos";
import visibilityFilter from "./visibilityFilter";
// import { connectRouter } from 'connected-react-router'

export default combineReducers({
    // router: connectRouter(history),
    todos,
    visibilityFilter,
});
