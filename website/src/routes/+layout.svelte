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
            <strong class="text-xl">Decentral Digest</strong>
        </svelte:fragment>

        <svelte:fragment slot="trail">
            <a
                class="variant-ghost-surface btn btn-sm"
                href="https://discord.gg/EXqV7W8MtY"
                target="_blank"
                rel="noreferrer"
            >
                Discord
            </a>
            <a
                class="variant-ghost-surface btn btn-sm"
                href="https://twitter.com/SkeletonUI"
                target="_blank"
                rel="noreferrer"
            >
                Twitter
            </a>
            <a
                class="variant-ghost-surface btn btn-sm"
                href="https://github.com/skeletonlabs/skeleton"
                target="_blank"
                rel="noreferrer"
            >
                GitHub
            </a>
        </svelte:fragment>
    </AppBar>

    <slot />
</AppShell>
