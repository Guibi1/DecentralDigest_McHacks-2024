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
    }

    onMount(fetchReadStatus);
</script>

<main class="container mx-auto flex max-w-screen-md flex-col gap-2 py-4">
    <ol class="breadcrumb mb-2">
        <li class="crumb"><a class="anchor" href="/">Home</a></li>
        <li class="crumb-separator" aria-hidden>&rsaquo;</li>
        <li class="crumb"><a class="anchor" href="/articles">News</a></li>
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

    <hr class="my-4 !border-secondary-500" />

    {#each data.text as text}
        <p class="p">
            {text}
        </p>
    {/each}

    <hr class="my-4 !border-secondary-500" />

    <section>
        <h2 class="text-xl">Mark as read</h2>

        <div class="flex gap-4">
            <aside class="alert variant-ghost-secondary w-full">
                <!-- Message -->
                <div class="alert-message">
                    <h3 class="h3">Mark as read</h3>
                    <p>You can use your crypto wallet to mark this article as read.</p>
                </div>

                <!-- Actions -->
                <div class="alert-actions">
                    {#if !$user.loggedIn}
                        <button on:click={user.login} class="variant-filled-secondary btn my-2">
                            Login with Flow
                        </button>
                    {:else}
                        {#await isRead}
                            <span> Loading... </span>
                        {:then isRead}
                            {#if isRead}
                                <span> Marked as read! </span>
                            {:else}
                                <button
                                    on:click={() => user.markAsRead(data.cid)}
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
        </div>
    </section>
</main>
