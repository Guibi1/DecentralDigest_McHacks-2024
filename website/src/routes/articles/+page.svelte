<script lang="ts">
    import Star from "$lib/Star.svelte";

    const articles = [
        {
            url: "QmS2m9qTYVzu3D4gNWnKfMabVFUYFE4dPKN3zGFgw9cjHX",
            title: "Sinner Upsets Medvedev in Epic AO Final, Wins First Slam at 22.",
        },
        {
            url: "QmbEj9wMSvLooaMzaASPdwQW9AFSeurLFM2cgHssk7L2F9",
            title: "Ukraine POWs: Mystery of Downed Plane",
        },
        {
            url: "QmYrxc7Gd1nLHNvqGiggbvt5ckAkwhg82ePZayEBaMTKxy",
            title: "US Troops Killed in Jordan Drone Attack",
        },
        {
            url: "QmPvgvfzBNASC5bBEpAda9N6EVmbr9h4XNh7RGc2yjDLHK",
            title: "Israel-Hamas Conflict: Gaza's Humanitarian Crisis Amid Aid Suspension and ICJ Genocide Allegations.",
        },
        {
            url: "QmVDKEVfi7webL57fADyuQZNDaFAbSCniXoLHs2VX1Drps",
            title: "Deepfake Swift Images Spark Concern, Calls for Legislation",
        },
        {
            url: "QmPk42MDPbeFcHsQZaUuPvSqNRZajSWcDEHPXCeG6NVQHw",
            title: "Paris Protests: Climate Activists Target Mona Lisa, Farmers Threaten Blockades",
        },
        {
            url: "QmVB92bVAuiT6jMvnFt3aK48BpXuAj2oeB4FEYvZuvhRTp",
            title: "Haley Criticizes RNC for Bias, Demands Fair Primary",
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
