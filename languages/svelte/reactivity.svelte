<!-- https://learn.svelte.dev/tutorial/reactive-declarations -->

<script>
	let count = 0;
  $: doubled = count * 2

	function increment() {
		count += 1;
	}
</script>

<!-- Example: clicked 11 times -->
<button on:click={increment}>
	Clicked {count}
	{count === 1 ? 'time' : 'times'}
</button>

<!-- 11 doubled is 22 -->
<p>{count} double is {doubled}</p> 