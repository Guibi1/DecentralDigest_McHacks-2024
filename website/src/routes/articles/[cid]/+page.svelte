<script lang="ts">
    import ClockIcon from "$lib/ClockIcon.svelte";
    import DateIcon from "$lib/DateIcon.svelte";
    import user from "$lib/flow";
    import { onMount } from "svelte";
    import type { PageData } from "./$types";

    export let data: PageData;

    let isRead: Promise<boolean>;

    async function fetchReadStatus() {
        isRead = user.getReadStatus(data.cid);
        return await isRead;
    }

    onMount(fetchReadStatus);
</script>

<main class="container mx-auto flex max-w-screen-md flex-col gap-2 py-4">
    <ol class="breadcrumb mb-2">
        <li class="crumb"><a class="variant-filled-secondary chip" href="/">Home</a></li>
        <li class="crumb-separator" aria-hidden>&rsaquo;</li>
        <li class="crumb"><a class="variant-filled-secondary chip" href="/articles">News</a></li>
        <li class="crumb-separator" aria-hidden>&rsaquo;</li>
        <li>Article</li>
    </ol>

    <h1 class="h1 mb-4">{data.title}</h1>

    <div class="flex gap-8">
        <div class="flex items-center gap-2">
            <ClockIcon />
            {data.time.text}
        </div>

        <div class="flex items-center gap-2">
            <DateIcon />
            {data.date.toLocaleDateString("ca-fr")}
        </div>
    </div>

    <h3 class="h3 mt-4">Sources</h3>

    <div class="flex gap-2">
        {#each data.sources as source, i}
            <a href={source} class="chip variant-ghost-tertiary">{i + 1}</a>
        {/each}
    </div>

    <hr class="!border-secondary-500 my-4" />

    {#each data.text as text}
        <p class="p">
            {text}
        </p>
    {/each}

    <aside class="alert variant-ghost-secondary mt-8 w-full">
        <!-- Message -->
        <div class="alert-message">
            <h3 class="h3">Mark as read</h3>
            <p>You can use your crypto wallet to mark this article as read.</p>
        </div>

        <!-- Actions -->
        <div class="alert-actions">
            {#if !$user.loggedIn}
                <button
                    on:click={async () => {
                        await user.login;
                        fetchReadStatus();
                    }}
                    class="variant-filled-secondary btn my-2"
                >
                    Login with Flow
                </button>
            {:else}
                {#await isRead}
                    <span> Loading... </span>
                {:then read}
                    {#if read}
                        <span> Marked as read! </span>
                    {:else}
                        <button
                            on:click={() =>
                                (isRead = user.markAsRead(data.cid).then(fetchReadStatus))}
                            class="variant-filled-primary btn my-2"
                        >
                            Mark as read
                        </button>
                    {/if}

                    <button on:click={user.logout} class="variant-ghost-error btn my-2">
                        Log out
                    </button>
                {/await}
            {/if}
        </div>
    </aside>
</main>
