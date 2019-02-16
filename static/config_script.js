document.getElementById('form-config').addEventListener('submit', (e) => {
    e.preventDefault();
    axios.post(
        '/config', 
        {
            'gender': parseInt(document.querySelector('input[name="gender"]:checked').value),
            'category': parseInt(document.querySelector('input[name="category"]:checked').value),
            'websites': collectWebsiteInputs()
        }
    ).then(function(res) {
        window.location = res.data;
    })
  });

  function collectWebsiteInputs() {
    var websites = document.getElementById("container-websites").getElementsByTagName("input")
    return [].slice.call(websites).filter(website => website.checked).map(website => parseInt(website.name));
  }
