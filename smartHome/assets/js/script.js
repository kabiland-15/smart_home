const hideBanners = () => {
  document.querySelectorAll('.banner.visible').forEach((b) => b.classList.remove('visible'));
};

var banners = [];

{% for message in messages %}
  var type = '{{ message.tags }}';
  var icon, class;
  if (type == 'error') {
    icon = 'alert-circle-outline';
    class = 'error';
  } else if (type == 'success') {
    icon = 'checkmark-circle-outline';
    class = 'success';
  } else if (type == 'info') {
    icon = 'info-outline';
    class = 'info';
  }
  banners.push({ icon: icon, class: class, message: '{{ message }}' });
{% endfor %}

// Show the banners based on the messages from Django
banners.forEach(banner => {
  const bannerElement = document.querySelector('.banner.' + banner.class);
  bannerElement.querySelector('.banner-message').innerText = banner.message;
  bannerElement.classList.add('visible');
});