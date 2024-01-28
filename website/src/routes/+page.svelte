<script lang="ts">
    import { onMount } from "svelte";

    const keywords = [
        "unbiased",
        "decentralized",
        "disruptive",
        "transparent",
        "insightful",
        "open",
        "real",
    ];

    let current = Math.floor(Math.random() * keywords.length);

    onMount(() => {
        setInterval(() => {
            current = (current + 1) % keywords.length;
        }, 2000);
    });
</script>

<div class="flex h-full flex-1 flex-col items-center justify-center gap-24">
    <h1 class="h1 flex flex-col items-center gap-2 font-bold">
        <div class="relative mb-8">
            {#each keywords as keyword, i}
                <span
                    class={`absolute -translate-x-1/2 -translate-y-1/2 transition-opacity duration-500 ${current === i ? "opacity-100" : "opacity-0"}`}
                >
                    {keyword}
                </span>
            {/each}
        </div>

        <div
            class="left-1/2 top-1/2 bg-gradient-to-br from-tertiary-500 to-secondary-500 box-decoration-clone bg-clip-text text-7xl text-transparent"
        >
            news
        </div>

        <span class="text-2xl italic"> for everyone </span>
    </h1>

    <a href="/articles" class="variant-filled-secondary btn btn-xl"> Browse articles</a>
</div>

<div class="square-grid-effect" />
