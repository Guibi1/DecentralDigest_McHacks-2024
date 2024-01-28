import { redirect } from "@sveltejs/kit";
import readingTime from "reading-time";
import { z } from "zod";
import type { PageServerLoad } from "./$types";

const articleSchema = z.object({
    title: z.string(),
    date: z.coerce.date(),
    text: z.string(),
    sources: z.string().array(),
});

export const load = (async ({ params, fetch }) => {
    const res = await fetch(`http://3.143.115.147:8080/ipfs/${params.cid}`);
    if (!res.ok) throw redirect(302, "/articles");

    const data = await res.json();
    const article = articleSchema.safeParse(data);

    if (!article.success) throw redirect(302, "/articles");
    return {
        ...article.data,
        cid: params.cid,
        title: article.data.title.replace(/^\s*"*|\s*"*$/g, ""),
        text: article.data.text.split("\n"),
        time: readingTime(article.data.text),
    };
}) satisfies PageServerLoad;
