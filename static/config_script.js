document.getElementById('form-config').addEventListener('submit', (e) => {
    e.preventDefault();
    document.cookie = "gender_id=" + parseInt(document.querySelector('input[name="gender_id"]:checked').value);
    document.cookie = "category_id=" + parseInt(document.querySelector('input[name="category_id"]:checked').value);
    document.cookie = "website_ids=" + collectWebsiteInputs();
    window.location = "/";
  });

function collectWebsiteInputs() {
  var websites = document.getElementById("container-websites").getElementsByTagName("input")
  return [].slice.call(websites).filter(website => website.checked).map(website => parseInt(website.name));
}