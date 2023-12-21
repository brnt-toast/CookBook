<!-- https://learn.svelte.dev/tutorial/spread-props -->

<script>
	import PackageInfo from './PackageInfo.svelte';

	const pkg = {
		name: 'svelte',
		version: 3,
		speed: 'blazingly',
		website: 'https://svelte.dev'
	};
</script>

<PackageInfo
	name={pkg.name}
	version={pkg.version}
	speed={pkg.speed}
	website={pkg.website}
/>
