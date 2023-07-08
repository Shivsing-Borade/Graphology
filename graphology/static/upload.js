const dropArea = document.getElementById('drop-area');
    const fileInput = document.getElementById('file-input');
    const fileLabel = document.getElementById('file-label');
    const fileInfo = document.getElementById('file-info');

    dropArea.addEventListener('dragenter', highlight);
    dropArea.addEventListener('dragover', highlight);
    dropArea.addEventListener('dragleave', unhighlight);
    dropArea.addEventListener('drop', handleDrop);
    fileInput.addEventListener('change', handleFile);

    function highlight(e) {
      e.preventDefault();
      dropArea.classList.add('highlight');
    }

    function unhighlight(e) {
      e.preventDefault();
      dropArea.classList.remove('highlight');
    }

    function handleDrop(e) {
      e.preventDefault();
      dropArea.classList.remove('highlight');
      const files = e.dataTransfer.files;
      showFile(files[0]);
    }

    function handleFile(e) {
      const files = e.target.files;
      showFile(files[0]);
    }

    function showFile(file) {
  fileInfo.innerHTML = '';
  const img = document.createElement('img');
  img.src = URL.createObjectURL(file);
  const name = document.createElement('p');
  name.textContent = `File Name: ${file.name}`;
  const size = document.createElement('p');
  size.textContent = `File Size: ${(file.size / 1024).toFixed(2)} KB`;
  fileInfo.appendChild(img);
  fileInfo.appendChild(name);
  fileInfo.appendChild(size);
  fileInfo.style.display = 'block';

  const waitText = document.createElement('p');
  waitText.style.fontWeight = 'bold';
  waitText.textContent = 'Wait for 5 seconds';
  fileInfo.insertBefore(waitText, img);

  dropArea.classList.add('hide');
  fileLabel.classList.add('hide');
  setTimeout(function() {
    dropArea.style.display = 'none';
    fileLabel.style.display = 'none';
  }, 5000);
}