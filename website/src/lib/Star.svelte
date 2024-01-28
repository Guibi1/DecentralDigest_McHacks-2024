<script lang="ts">
    const colors = ["stroke-primary-500", "stroke-secondary-500", "stroke-tertiary-500"];
    const index = Math.floor(Math.random() * colors.length);

    export let styles = "";
</script>

<svg
    width="5rem"
    height="5rem"
    viewBox="0 0 300 300"
    xmlns="http://www.w3.org/2000/svg"
    class={`fixed ${styles} stroke-2 ${colors[index]}`}
>
    <g>
        <line id="svg_10" y2="150" x2="300" y1="150" x1="0" />
        <line transform="rotate(20, 150, 150)" id="svg_11" y2="150" x2="300" y1="150" x1="0" />
        <line transform="rotate(40, 150, 150)" id="svg_12" y2="150" x2="300" y1="150" x1="0" />
        <line transform="rotate(60, 150, 150)" id="svg_13" y2="150" x2="300" y1="150" x1="0" />
        <line transform="rotate(80, 150, 150)" id="svg_14" y2="150" x2="300" y1="150" x1="0" />
        <line transform="rotate(100, 150, 150)" id="svg_15" y2="150" x2="300" y1="150" x1="0" />
        <line transform="rotate(120, 150, 150)" id="svg_16" y2="150" x2="300" y1="150" x1="0" />
        <line transform="rotate(140, 150, 150)" id="svg_17" y2="150" x2="300" y1="150" x1="0" />
        <line transform="rotate(160, 150, 150)" id="svg_18" y2="150" x2="300" y1="150" x1="0" />
    </g>
</svg>
