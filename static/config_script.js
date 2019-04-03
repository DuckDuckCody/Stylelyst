document.getElementById('form-config').addEventListener('submit', (e) => {
    e.preventDefault();
    document.cookie = "gender=" + parseInt(document.querySelector('input[name="gender"]:checked').value);
    document.cookie = "category=" + parseInt(document.querySelector('input[name="category"]:checked').value);
    document.cookie = "websites=" + collectWebsiteInputs();
    window.location = "/";
  });

  function collectWebsiteInputs() {
    var websites = document.getElementById("container-websites").getElementsByTagName("input")
    return [].slice.call(websites).filter(website => website.checked).map(website => parseInt(website.name));
  }
