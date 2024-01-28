<script lang="ts">
    const logos = [
        {
            name: "SvelteKit",
            description:
                "A concise web framework with    reactive components. It prioritizes simplicity and optimal performance for building modern web applications.",
            src: "https://a.storyblok.com/f/88751/1702x2049/619c584101/svelte_logo.png",
            link: "https://kit.svelte.dev/",
        },
        {
            name: "IPFS",
            description:
                "A decentralized and distributed protocol. It's a more resilient and efficient way to store and share data on the internet, while ensuring integrity and authenticity.",
            src: "https://ipfs.tech/_nuxt/ipfs-logo.a313bcee.svg",
            link: "https://ipfs.tech/",
        },
        {
            name: "Mistral AI",
            description:
                "A small, fast and unrestricted language model that can be trained to optimise even further. It competes with ChatGPT while being magnitudes faster and cheaper to run.",
            src: "https://mistral.ai/images/logo_hubc88c4ece131b91c7cb753f40e9e1cc5_2589_256x0_resize_q97_h2_lanczos_3.webp",
            link: "https://mistral.ai/",
        },
        {
            name: "SpaCy",
            description:
                "An open-source natural language processing library developed in Python and Cython for production usage. It allows to train AI faster and with more precision.",
            src: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/SpaCy_logo.svg/2560px-SpaCy_logo.svg.png",
            link: "https://spacy.io/",
        },
    ];
</script>

<main class="container mx-auto flex h-full flex-col items-center gap-4 py-4">
    <h1 class="h1">About us</h1>

    <div class="max-w-2xl text-center">
        <p class="p">DecentralDigest aims to be your go-to source for news all around the world!</p>

        <p class="p">
            Having a second point of view is crution in this era of desinformation. That's why our
            mission is to provide accurate and up-to-date information about the politics and the
            world. We use news report from real and trust-worthy news websites, and correct and
            point out the biases.
        </p>
    </div>

    <h2 class="h2 mt-2">Technologies</h2>

    <div class="logo-cloud my-2 grid-cols-1 gap-8 md:!grid-cols-2 xl:!grid-cols-4">
        {#each logos as { src, name, description, link }}
            <a
                class="logo-item variant-ghost-primary flex w-64 flex-col gap-4 p-4"
                href={link}
                target="_blank"
                rel="noopener noreferrer"
            >
                <img class="aspect-square h-20 object-contain" {src} alt="The Svelte logo" />
                <span class="!m-0">{name}</span>
                <span class="!m-0 font-normal"> {description} </span>
            </a>
        {/each}
    </div>
</main>
