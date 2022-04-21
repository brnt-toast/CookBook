// ...Upgrade to React 18
// https://reactjs.org/blog/2022/03/08/react-18-upgrade-guide.html
// --

import {createRoot} from 'react-dom/client';
import from App from './App';

const root = createRoot(
	document.querySelector('#app')
);

root.render(
	<App />
)
