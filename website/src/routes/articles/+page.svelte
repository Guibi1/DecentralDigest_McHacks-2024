<script lang="ts">
    import Star from "$lib/Star.svelte";

    const articles = [
        {
            title: "Jannik Sinner Makes History: 22-Year-Old Italian Defeats Daniil Medvedev in Thrilling Australian Open Final Comeback, Becomes Youngest Men's Grand Slam Winner Since Djokovic in 2008",
            url: "QmeN28evEeSs1FTs3gW1rkUjn31GNPTAzMWzxBfyJjgHnU",
        },
        {
            title: "Former President Trump Ordered to Pay $83.3 Million in Damages to E. Jean Carroll Over Defamation Verdict",
            url: "QmaPC9kXhj6SwLVBgyWQeGdpwajhoSx8RoEGjAu1fqyt5h",
        },
        {
            title: "Ongoing Conflict in Gaza: UN Calls for Humanitarian Aid Amidst Accusations of International Law Violations and Genocide",
            url: "QmSwPLww9YunmT1uHABAT61DZegmKki3SPe4CCtGZazCgC",
        },
        {
            title: "Sinner Stuns Medvedev in Australian Open Final Comeback: Italian Claims First Grand Slam Title After Epic Five-Set Victory\" This title highlights the dramatic comeback of Jannik Sinner, who was down two sets and rallied to win the Australian Open final against Daniil Medvedev. It also emphasizes Sinner's achievement in winning his first Grand Slam title at the young age of 22.",
            url: "QmYLpmaBKuDpFY8eNpdnq5LsmDFwqAXJYLzsuCKqVVaZ9D",
        },
        {
            title: "Jannik Sinner Makes History: 22-Year-Old Italian Defeats Daniil Medvedev in Thrilling Australian Open Final Comeback, Becomes Youngest Men's Grand Slam Winner Since Djokovic in 2008",
            url: "QmfWiRLvXfH4iAZr2dTYJeqF4Pr2ER4Byhv7cdsToQxU7t",
        },
        {
            title: "Ongoing Conflict in Gaza: UN Calls for Humanitarian Aid Amidst Accusations of International Law Violations and Genocide",
            url: "QmQcr8thxDWsyFTsNvPV9i2grRt8yBrvFc3Th67KS23XSq",
        },
        {
            title: "Swift Deepfakes Sparks Outrage: Experts Demand Legislation to Combat AI-Generated Explicit Imagery",
            url: "QmWza81aV22RYE4iY1DKugXySdXktBaait81FnB8joQCyA",
        },
        {
            title: "Former President Trump Ordered to Pay $83.3 Million in Damages to E. Jean Carroll Over Defamation Verdict: The Largest Award for a Single Plaintiff in U.S. Defamation History",
            url: "QmYDRAPww24Aj3P7joHLKyQoVF7Rz74Az5sgKbewE9PF2m",
        },
        {
            title: "ing Charles III's Prostate Surgery Sparks Awareness: Encouraging Men to Seek Medical Attention for BPH",
            url: "QmNTDT1BZ8VEEjD6ZTTfVQK3ZmTyD8B78wswHTRtBkftdH",
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
