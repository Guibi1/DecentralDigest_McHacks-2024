import { z } from "zod";
import type { PageServerLoad } from "./$types";

const articleSchema = z.object({
    title: z.string(),
    content: z.string(),
    replacements: z.array(
        z.object({
            new: z.string(),
            old: z.string(),
            source: z.string(),
        })
    ),
});

export const load = (async ({ params, fetch }) => {
    const res = await fetch(`http://ipfs.decentraldigest.co:8080/ipfs/${params.cid}`);
    if (!res.ok) throw new Error("Not found");

    const data = await res.json();
    const article = articleSchema.safeParse(data);

    if (!article.success) throw new Error("Invalid article");

    let content: (string | z.infer<typeof articleSchema>["replacements"][number])[] = [];

    article.data.replacements.forEach((replacement) => {
        const text = (content.at(-1) as string) ?? article.data.content;
        const [before, ...after] = text.split(replacement.new);

        content = [before, replacement, after.join(replacement.new)];
    });

    return { title: article.data.title, content };
}) satisfies PageServerLoad;
