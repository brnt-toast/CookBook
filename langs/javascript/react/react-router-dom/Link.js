import React from 'react';
import {Routes, Route, Link} from 'react-router-dom';

import Home from './pages/Home'

export default function App(){
	return (
		<>
			<h1> Hello from App.js </h1>
			<Link exact to="/"> Home </Link>

			<hr />

			<Routes>
				<Route path="/" element={<Home />} />	
			</Routes>
		</>
	)
}
