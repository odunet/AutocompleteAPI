//Initialize DOM objects
let inp = document.getElementById('inp');
let result = document.getElementById('result');

//Event listener for keyup in the input element
inp.addEventListener('keyup', async (e) => {
  result.innerHTML = '';
  let inpList = inp.value.split(' ');
  let data = await fetch(
    `http://127.0.0.1:5000/api/${inpList[inpList.length - 1]}`
  );

  let cleanData = await data.json();

  if (cleanData.length < 1) {
    result.style.display = 'none';
  } else {
    result.style.display = '';

    for (const i in cleanData) {
      let item = document.createElement('p');
      item.innerHTML = cleanData[i];
      item.classList.add('item');
      result.appendChild(item);

      item.addEventListener('click', (e) => {
        inpList[inpList.length - 1] = item.innerHTML;
        inp.value = inpList.join(' ') + ' ';
        result.style.display = 'none';
      });
    }
  }
});
