<script lang="ts">
    import type { PageData } from "./$types";
    import { popup, type PopupSettings } from "@skeletonlabs/skeleton";

    export let data: PageData;

    const popupHover = (target: string) =>
        ({
            event: "hover",
            target,
            placement: "top",
        }) satisfies PopupSettings;
</script>

<h1 class="h1">{data.title}</h1>

<p class="p">
    {#each data.content as content, i}
        {#if typeof content === "string"}
            {content}
        {:else}
            <span class="a" use:popup={popupHover(`${i}`)}>
                <span>{content.new}</span>
            </span>

            <div class="card variant-filled-secondary p-4" data-popup={`${i}`}>
                <p>{content.old}</p>
                <p>from {content.source}</p>
                <div class="variant-filled-secondary arrow" />
            </div>
        {/if}
    {/each}
</p>
