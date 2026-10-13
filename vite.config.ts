import { defineConfig } from "vite";

export default defineConfig({
  base: "./",
  build: {
    // The page loads the fleet with a top-level await before building the HUD.
    target: "es2022",
    outDir: "dist",
    emptyOutDir: true,
    rollupOptions: {
      // Resolved at runtime by the page's import map to ./vendor (public/).
      external: [/^three(\/.*)?$/],
    },
  },
});
