// You can also use the generator at https://skeleton.dev/docs/generator to create these values for you
import type { CustomThemeConfig } from "@skeletonlabs/tw-plugin";
export const theme: CustomThemeConfig = {
    name: "theme",
    properties: {
        // =~= Theme Properties =~=
        "--theme-font-family-base": `Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'`,
        "--theme-font-family-heading": `Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'`,
        "--theme-font-color-base": "0 0 0",
        "--theme-font-color-dark": "255 255 255",
        "--theme-rounded-base": "4px",
        "--theme-rounded-container": "4px",
        "--theme-border-base": "2px",
        // =~= Theme On-X Colors =~=
        "--on-primary": "0 0 0",
        "--on-secondary": "255 255 255",
        "--on-tertiary": "0 0 0",
        "--on-success": "0 0 0",
        "--on-warning": "0 0 0",
        "--on-error": "255 255 255",
        "--on-surface": "255 255 255",
        // =~= Theme Colors  =~=
        // primary | #4ceba2
        "--color-primary-50": "228 252 241", // #e4fcf1
        "--color-primary-100": "219 251 236", // #dbfbec
        "--color-primary-200": "210 250 232", // #d2fae8
        "--color-primary-300": "183 247 218", // #b7f7da
        "--color-primary-400": "130 241 190", // #82f1be
        "--color-primary-500": "76 235 162", // #4ceba2
        "--color-primary-600": "68 212 146", // #44d492
        "--color-primary-700": "57 176 122", // #39b07a
        "--color-primary-800": "46 141 97", // #2e8d61
        "--color-primary-900": "37 115 79", // #25734f
        // secondary | #ab2fca
        "--color-secondary-50": "242 224 247", // #f2e0f7
        "--color-secondary-100": "238 213 244", // #eed5f4
        "--color-secondary-200": "234 203 242", // #eacbf2
        "--color-secondary-300": "221 172 234", // #ddacea
        "--color-secondary-400": "196 109 218", // #c46dda
        "--color-secondary-500": "171 47 202", // #ab2fca
        "--color-secondary-600": "154 42 182", // #9a2ab6
        "--color-secondary-700": "128 35 152", // #802398
        "--color-secondary-800": "103 28 121", // #671c79
        "--color-secondary-900": "84 23 99", // #541763
        // tertiary | #5bd8d8
        "--color-tertiary-50": "230 249 249", // #e6f9f9
        "--color-tertiary-100": "222 247 247", // #def7f7
        "--color-tertiary-200": "214 245 245", // #d6f5f5
        "--color-tertiary-300": "189 239 239", // #bdefef
        "--color-tertiary-400": "140 228 228", // #8ce4e4
        "--color-tertiary-500": "91 216 216", // #5bd8d8
        "--color-tertiary-600": "82 194 194", // #52c2c2
        "--color-tertiary-700": "68 162 162", // #44a2a2
        "--color-tertiary-800": "55 130 130", // #378282
        "--color-tertiary-900": "45 106 106", // #2d6a6a
        // success | #84cc16
        "--color-success-50": "237 247 220", // #edf7dc
        "--color-success-100": "230 245 208", // #e6f5d0
        "--color-success-200": "224 242 197", // #e0f2c5
        "--color-success-300": "206 235 162", // #ceeba2
        "--color-success-400": "169 219 92", // #a9db5c
        "--color-success-500": "132 204 22", // #84cc16
        "--color-success-600": "119 184 20", // #77b814
        "--color-success-700": "99 153 17", // #639911
        "--color-success-800": "79 122 13", // #4f7a0d
        "--color-success-900": "65 100 11", // #41640b
        // warning | #e5a50a
        "--color-warning-50": "251 242 218", // #fbf2da
        "--color-warning-100": "250 237 206", // #faedce
        "--color-warning-200": "249 233 194", // #f9e9c2
        "--color-warning-300": "245 219 157", // #f5db9d
        "--color-warning-400": "237 192 84", // #edc054
        "--color-warning-500": "229 165 10", // #e5a50a
        "--color-warning-600": "206 149 9", // #ce9509
        "--color-warning-700": "172 124 8", // #ac7c08
        "--color-warning-800": "137 99 6", // #896306
        "--color-warning-900": "112 81 5", // #705105
        // error | #a51d2d
        "--color-error-50": "242 221 224", // #f2dde0
        "--color-error-100": "237 210 213", // #edd2d5
        "--color-error-200": "233 199 203", // #e9c7cb
        "--color-error-300": "219 165 171", // #dba5ab
        "--color-error-400": "192 97 108", // #c0616c
        "--color-error-500": "165 29 45", // #a51d2d
        "--color-error-600": "149 26 41", // #951a29
        "--color-error-700": "124 22 34", // #7c1622
        "--color-error-800": "99 17 27", // #63111b
        "--color-error-900": "81 14 22", // #510e16
        // surface | #101010
        "--color-surface-50": "219 219 219", // #dbdbdb
        "--color-surface-100": "207 207 207", // #cfcfcf
        "--color-surface-200": "195 195 195", // #c3c3c3
        "--color-surface-300": "159 159 159", // #9f9f9f
        "--color-surface-400": "88 88 88", // #585858
        "--color-surface-500": "16 16 16", // #101010
        "--color-surface-600": "14 14 14", // #0e0e0e
        "--color-surface-700": "12 12 12", // #0c0c0c
        "--color-surface-800": "10 10 10", // #0a0a0a
        "--color-surface-900": "8 8 8", // #080808
    },
};
