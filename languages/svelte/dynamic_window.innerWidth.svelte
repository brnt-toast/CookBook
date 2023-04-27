<script>
  import {onMount} from 'svelte'
  const width = () => window.innerWidth     // get the width of the window

  onMount(() => {
    window.addEventListener('resize', ()=>{ // add event listener to the window
      console.log(width())                  // console.log the width function every time the window is resized
    })
  })
</script>

<h1>Hello World</h1>
<p>{width()}</p>

<style>
  h1 {
    color:red;
  }
</style>
