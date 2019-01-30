import React from "react";
import { Fragment } from "react";

const selectedPhotoStyle = {
    "margin-left": "30px",
    "font-weight": "bold",
};

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            photoBaseURL: "http://127.0.0.1:5000/photos/",
            filenames: [],
            currentPhoto: ""
        };
        this.fetchFilenames = this.fetchFilenames.bind(this);
    }

    fetchFilenames() {
        fetch("http://localhost:5000/api/photos/")
          .then(response => response.json())
          .then((data) => {
              this.setState({ filenames: data.filenames })
              this.setState({ currentPhoto: data.filenames[0] })
          })
    }

    componentDidMount() {
        this.fetchFilenames();
        this.interval = setInterval(this.fetchFilenames, 5000);
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }

    render() {
        return(
          <Fragment>
              <img id="image" src={this.state.photoBaseURL + this.state.currentPhoto} alt="timeframe"/>
              <ul>
                  {this.state.filenames.map((filename) => (
                      <li key={filename}
                          style={filename === this.state.currentPhoto ? selectedPhotoStyle : null}
                          onClick={() => {this.setState({currentPhoto: filename})}}>
                          {filename}
                      </li>
                  ))}
              </ul>
          </Fragment>
        )
    }

}

export default App;
