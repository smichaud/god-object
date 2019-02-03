import React from "react";
import { Fragment } from "react";

const listStyle = {
    "float": "left",
};

const selectedPhotoStyle = {
    "fontSize": "120%",
    "fontWeight": "bold",
};

const imageStyle = {
    "float": "right",
    "marginRight": "10%",
};

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            photoBaseURL: "http://172.16.20.100:5000/photos/",
            filenames: [],
            currentPhoto: "0000-placeholder.jpg",
            isSetLatest: true,
        };
        this.fetchFilenames = this.fetchFilenames.bind(this);
    }

    fetchFilenames() {
        fetch("http://172.16.20.100:5000/api/photos/")
          .then(response => response.json())
          .then((data) => {
              this.setState({ filenames: data.filenames });
              if (this.state.isSetLatest) {
                  this.setState({ currentPhoto: data.filenames[0] });
              }
          })
    }

    componentDidMount() {
        this.fetchFilenames();
        this.interval = setInterval(this.fetchFilenames, 2000);
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }

    render() {
        return(
          <Fragment>
              <ul style={listStyle}>
                  {this.state.filenames.map((filename) => (
                      <li key={filename}
                          style={filename === this.state.currentPhoto ? selectedPhotoStyle : null}
                          onClick={() => {
                              if (filename !== this.state.filenames[0]) {
                                  this.setState({isSetLatest: false});
                              } else {
                                  this.setState({isSetLatest: true});
                              }
                              this.setState({currentPhoto: filename});
                          }}>
                          {filename}
                      </li>
                  ))}
              </ul>
              <img id="image" style={imageStyle} src={this.state.photoBaseURL + this.state.currentPhoto} alt="timeframe"/>
          </Fragment>
        )
    }

}

export default App;
