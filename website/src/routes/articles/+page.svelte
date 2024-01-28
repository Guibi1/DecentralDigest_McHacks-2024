<script lang="ts">
    const articles = [
        {
            title: "Deepfakes of Taylor Swift and George Carlin Raise Concerns: Legal Protections and AI Regulation Needed",
            url: "Qmaq93GmDssaGDbh2ZthpJ1zWLNEyEPpYc3YCyxnmtbyrj",
        },
    ];
</script>

<main class="container mx-auto flex flex-col px-16">
    {#each articles as article}
        <a href={`/articles/${article.url}`}>
            <div class="card variant-ghost-primary max-w-lg p-4">
                <span class="h3">{article.title}</span>
            </div>
        </a>
    {/each}
</main>
