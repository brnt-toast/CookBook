<!-- https://learn.svelte.dev/tutorial/reactive-statements -->

<script>
    let count = 0

    // statments are valid
    $: console.log(`the count is ${count}`)

    function handleClick() {
        count +1;
    }

    // statemetns can be blocked
    $: {
        console.log(`the count is ${count}`)
        alert(`I SAID THE COUNT IS ${count}`)
    }

    // including if blocks
    $: if (count >= 10){
        alert('count is dangerously high!')
        count = 0
    }
</script>

<button on:click={handleClick}>
    Clicked {count}
    {count === 1 ? 'time' : 'times'}
</button>