<script>
  import Grid from "svelte-grid";
  import gridHelp from "svelte-grid/build/helper/index.mjs";
  import Plot from "./Plot.svelte";
	import { fly } from 'svelte/transition';

  const id = () =>
    "_" +
    Math.random()
      .toString(36)
      .substr(2, 9);

  let items = [
    gridHelp.item({
      x: 0,
      y: 0,
      w: 2,
      h: 2,
      id: id(),
      desc: "Number of windmills",
      val: 5.3,
      img_src: "windmill.png",
      color: "#8BC34A"
    }),
    gridHelp.item({
      x: 2,
      y: 0,
      w: 2,
      h: 2,
      id: id(),
      desc: "Barrels of oil",
      val: 15.0,
      img_src: "oil.png",
      color: "#00BCD4"
    }),
    gridHelp.item({
      x: 0,
      y: 2,
      w: 2,
      h: 2,
      id: id(),
      desc: "Amount of EV cars",
      val: 12.0,
      img_src: "electric_car.png",
      color: "#FFEB3B"
    }),
    gridHelp.item({
      x: 2,
      y: 2,
      w: 2,
      h: 2,
      id: id(),
      desc: "Number of stop light pull ups",
      val: 130.0,
      img_src: "drag_race.png",
      color: "#009688"
    })
  ];

  let show_comparisons = false;
</script>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
  .content {
    width: 100%;
    height: 100%;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: large;
    font-size: 2vw;
    border-radius: 6px;
    border-bottom-right-radius: 3px;
  }
  :global(.svlt-grid-shadow) {
    background: pink;
    border-radius: 6px;
    border-bottom-right-radius: 3px;
    /*transition: top 0.2s, left 0.2s;*/
    transition: transform 0.2s;
  }
  :global(.svlt-grid-container) {
    /* border: 1px solid #aaa; */
    background: white;
  }

  .column {
    float: left;
    flex: 50%;
  }

  .row {
    display: flex;
    clear: both;
  }

  .comparison-val {
    font-size: x-large;
    font-size: 2vw;
    font-weight: bold;
  }
</style>

<main>
  <h1>SUV MONITOR NL</h1>

    <p>Number of SUVs bought per month</p>
    <Plot />
    <br />
  <label>
    <input type="checkbox" bind:checked={show_comparisons} />
    Hide these worrisome comparisons
  </label>

  {#if show_comparisons == false}
    <Grid {items} cols={4} let:item rowHeight={85} gap={10}>
      <div
        class="content"
        style="background: {item.static ? '#ccccee' : item.color}">
        <div class="row">
          <div class="column">
            <img
              src={item.img_src}
              alt={item.desc}
              style="display: block; width: 100%; height: auto; max-height:100px; max-width:100px;" />
          </div>
          <div class="column" style="align:left;">
            {item.desc}
            <br />
            <div class="comparison-val">{item.val}</div>
          </div>
        </div>

      </div>
    </Grid>
  {:else}
    <div transition:fly="{{ y: 200, duration: 2000 }}"><h1>Coward!</h1></div>
  {/if}

</main>
