import { defineConfig } from "vite";

export default defineConfig({
  base: "./",
  build: {
    outDir: "dist",
    emptyOutDir: true,
    rollupOptions: {
      // Resolved at runtime by the page's import map to ./vendor (public/).
      external: [/^three(\/.*)?$/],
    },
  },
});
