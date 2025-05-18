# Guidelines for Agents

This repository contains Python and JavaScript/TypeScript projects. Follow these steps whenever you modify the code.

## Python
- Use `black --line-length 550` for formatting.
- Run `flake8 --max-line-length=1024 --ignore=E402,E203,E722` on edited files.
- Verify the code compiles with `python -m py_compile <modified files>`.

## JavaScript/TypeScript
- Format files with Prettier using the repository `.prettierrc` settings. Example:
  ```bash
  npx prettier <files> --write
  ```
- If any file in `client/lib` or `client/demo` is changed, run `npm test` in the corresponding directory.

## Commit
- Ensure the repository is clean (`git status`) and all checks above pass before committing.
