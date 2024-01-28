<script lang="ts">
    import "../app.postcss";
    import { AppShell, AppBar } from "@skeletonlabs/skeleton";

    // Floating UI for Popups
    import { computePosition, autoUpdate, flip, shift, offset, arrow } from "@floating-ui/dom";
    import { storePopup } from "@skeletonlabs/skeleton";
    storePopup.set({ computePosition, autoUpdate, flip, shift, offset, arrow });
</script>

<AppShell>
    <AppBar slot="header" padding="p-8">
        <svelte:fragment slot="lead">
            <a class="text-xl" href="/">Decentral Digest</a>
        </svelte:fragment>

        <svelte:fragment slot="trail">
            <a class="variant-ghost-surface btn btn-sm" href="/articles"> News </a>
            <a class="variant-ghost-surface btn btn-sm" href="/about"> About </a>

            <a
                class="variant-ghost-surface btn btn-sm"
                href="https://github.com/Guibi1/DecentralDigest_McHacks-2024"
                target="_blank"
                rel="noreferrer"
            >
                GitHub
            </a>
        </svelte:fragment>
    </AppBar>

    <slot />
</AppShell>
