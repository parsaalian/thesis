module.exports = {
    "stories": [
        "../src/components/**/*.stories.@(js|jsx|ts|tsx|mdx)",
        "../src/containers/**/*.stories.@(js|jsx|ts|tsx|mdx)",
        "../src/pages/**/*.stories.@(js|jsx|ts|tsx|mdx)"
    ],
    "addons": [
        "@storybook/addon-links",
        "@storybook/addon-essentials",
        "@storybook/preset-create-react-app"
    ]
}