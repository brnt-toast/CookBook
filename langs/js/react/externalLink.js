import React from 'react';
import Linkify from 'react-linkify' // npm i linkify | external links

export default OutboundLink(){
	return (
		<>
			<p> Hello from OutboundLink.js </p>
			<Linkify>
				<a
					target="_blank" // new window
					href='https://github.com/tasti/react-linkify/'
				> Linkify  <a/>
			</Linkify>
		</>
	)
}
