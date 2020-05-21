// Remove the no JS class so that the button will show
document.documentElement.classList.remove('no-js');

const STORAGE_KEY = 'user-color-scheme';
const COLOR_MODE_KEY = '--color-mode';

const modeToggleButton = document.querySelector('.js-mode-toggle');
const modeToggleText = document.querySelector('.js-mode-toggle-text');
const modeStatusElement = document.querySelector('.js-mode-status');

/**
 * Pass in a custom prop key and this function will return its
 * computed value. 
 * A reduced version of this: https://andy-bell.design/wrote/get-css-custom-property-value-with-javascript/
 */
const getSSCustomProp = (propKey) => {
	let response = getComputedStyle(document.documentElement).getPropertyValue(propKey);

	// Tidy up the string if there’s something to work with
	if (response.length) {
		response = response.replace(/\'|"/g, '').trim();
	}

	// Return the string response by default
	return response;
};

/**
 * Takes either a passed settings ('light'|'dark') or grabs that from localStorage.
 * If it can’t find the setting in either, it tries to load the CSS color mode,
 * controlled by the media query
 */
const applySetting = passedSetting => {
	let currentSetting = passedSetting || localStorage.getItem(STORAGE_KEY);

	if(currentSetting) {
		document.documentElement.setAttribute('data-user-color-scheme', currentSetting);
		setButtonLabelAndStatus(currentSetting);
	}
	else {
		setButtonLabelAndStatus(getCSSCustomProp(COLOR_MODE_KEY));
	}
}

/**
 * Get’s the current setting > reverses it > stores it
 */
const toggleSetting = () => {
	let currentSetting = localStorage.getItem(STORAGE_KEY);

	switch(currentSetting) {
		case null:
			currentSetting = window.matchMedia('(prefers-color-scheme: dark)').matches ? "dark" : "light";
			break;
		case 'light':
			currentSetting = 'dark';
			break;
		case 'dark':
			currentSetting = 'light';
			break;
	}


	localStorage.setItem(STORAGE_KEY, currentSetting);
    console.log("switch theme: ", currentSetting);


	return currentSetting;
}

/**
 * A shared method for setting the button text label and visually hidden status element 
 */
const setButtonLabelAndStatus = currentSetting => { 
	modeToggleText.innerText = `${currentSetting === 'dark' ? '.' : '.'}`;
//	modeStatusElement.innerText = `Color mode is now "${currentSetting}"`;
}

/**
 * Clicking the button runs the apply setting method which grabs its parameter
 * from the toggle setting method.
 */
modeToggleButton.addEventListener('click', evt => {
	evt.preventDefault();
	applySetting(toggleSetting());
});

applySetting();

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
	const newColorScheme = e.matches ? "dark" : "light";
	if (newColorScheme != localStorage.getItem(STORAGE_KEY)) {
		e.preventDefault();
		applySetting(toggleSetting());

	} 
	
});
