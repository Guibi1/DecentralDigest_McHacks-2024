<script lang="ts">
    import Star from "$lib/Star.svelte";

    const articles = [
        {
            title: "Deepfakes of Taylor Swift and George Carlin Raise Concerns: Legal Protections and AI Regulation Needed",
            url: "Qmaq93GmDssaGDbh2ZthpJ1zWLNEyEPpYc3YCyxnmtbyrj",
        },
        {
            title: "Trump Ordered to Pay $83.3 Million in Damages to E. Jean Carroll for Defamation in Sexual Assault Case",
            url: "QmRgvwbeChb6Q9nErpJBg1idYx3dpEK8mbbRLJHUzXNTnH",
        },
        {
            title: "Reflect, Antisemitism Concerns Rise, and Auschwitz Preservation Efforts Continue",
            url: "QmYZZ4mUzy3opqQ8Xuu5aBN4jVuWf2MATuKM6gfFENcLuA",
        },
        {
            title: "Cardell Hayes Convicted of Manslaughter in Retrial for Killing Former New Orleans Saints Star Will Smith, Faces Up to 40 Years in Prison",
            url: "QmYuEQYH9R5T1HYz9BJPbB2NTaK9n9CgNffzSvKn8rWecw",
        },
    ];
</script>

<section class="container mx-auto mb-8 flex flex-col items-center gap-8 px-16">
    <h1 class="h1">News articles</h1>

    {#each articles as article}
        <a
            href={`/articles/${article.url}`}
            class="card variant-ghost-primary card-hover max-w-lg p-4"
        >
            <span class="h3">{article.title}</span>

            <footer class="mt-2 text-right">Visit ></footer>
        </a>
    {/each}
</section>

<Star styles="top-[20%] left-[20%]" />
<Star styles="top-[40%] left-[90%]" />
<Star styles="top-[92%] left-[10%]" />
<Star styles="top-[30%] left-[70%]" />
<Star styles="top-[75%] left-[40%]" />
<Star styles="top-[80%] left-[70%]" />
