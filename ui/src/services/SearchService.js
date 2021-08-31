import axios from "axios";

const API_PATH = "http://localhost:5000";
// const API_PATH = "http://localhost:5000";


export const serviceSearchAPI = (query) => {
    return new Promise(
        ((resolve, reject) => {
                axios.get(`${API_PATH}/search/${query}`).then((response) => {
                  resolve(response.data.hits.hits);
                });
            }
        )
    )
}
export const serviceSearchAsYouType = (query) => {
    return new Promise(
        ((resolve, reject) => {
                axios
                  .get(`${API_PATH}/saut/${query}`)
                  .then((response) => {
                    resolve(response.data.hits.hits);
                  })
                  .catch((err) => reject("Problem with server: " + err));
            }
        )
    )
}